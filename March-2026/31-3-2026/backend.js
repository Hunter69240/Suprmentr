import fetch from "node-fetch";
import dotenv from "dotenv";

dotenv.config();

const API_KEY = process.env.API_KEY;

export async function getExplanation(topic) {
    try {
        const response = await fetch("https://api.openai.com/v1/responses", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${API_KEY}`
            },
            body: JSON.stringify({
                model: "gpt-4.1-mini",
                input: `Explain the topic: ${topic} in simple terms`
            })
        });

        const data = await response.json();

        // debug actual response
        console.log(data);

        if (data.error) {
            console.log("API Error:", data.error.message);
            return;
        }

        return data.output?.[0]?.content?.[0]?.text;

    } catch (error) {
        console.log(error);
    }
}