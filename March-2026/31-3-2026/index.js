import { getExplanation } from "./backend.js";

async function run() {
    const topic = "Machine Learning";
    const result = await getExplanation(topic);
    console.log(result);
}

run();