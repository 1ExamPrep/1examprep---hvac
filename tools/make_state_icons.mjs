import fs from "fs";
import {feature} from "topojson-client";
import {geoPath, geoConicConformal, geoMercator} from "d3-geo";
const us = JSON.parse(fs.readFileSync(new URL("node_modules/us-atlas/states-10m.json", import.meta.url)));
const fc = feature(us, us.objects.states);
const want = JSON.parse(process.argv[2]); // {code: "Name"}
const out = process.argv[3]; fs.mkdirSync(out, {recursive: true});
const S = 100;
for (const [code, name] of Object.entries(want)) {
  const nm = code === "dc" ? "District of Columbia" : name;
  const f = fc.features.find(x => x.properties.name === nm);
  if (!f) { console.log("missing", code, name); continue; }
  const proj = (code === "hi" ? geoMercator() : geoConicConformal().parallels([30,45]).rotate([d3c(f)[0],0])).fitExtent([[4,4],[S-4,S-4]], f);
  let d = geoPath(proj)(f).replace(/(\d+\.\d)\d+/g, "$1");
  fs.writeFileSync(`${out}/${code}.svg`, `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${S} ${S}"><path d="${d}" fill="#021f4a"/></svg>`);
}
function d3c(f){ const b = geoPath().bounds(f); return [ -( (b[0][0]+b[1][0])/2 ), 0 ]; }
