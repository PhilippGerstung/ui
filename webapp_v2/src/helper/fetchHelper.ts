import type { z, ZodSchema } from "zod";

export async function get<T extends ZodSchema>(url: string, schema: T): Promise<z.infer<T>> {
    return new Promise((resolve, reject) => {
        fetch(url).then((response) => {
            if (response.ok) {
                response.json().then((data) => {
                    const parsed = schema.safeParse(data);
                    if (parsed.success) {
                        resolve(parsed.data);
                    }
                    else {
                        console.error(`Failed to parse data from ${url}`, parsed.error);
                        reject(parsed.error);
                    }
                });
            } else {
                console.error(`Failed to get ${url}`, response.status, response)
                reject(response.statusText);
            }
        }).catch((error) => {
            console.error(`Failed to fetch ${url}`, error);
            reject(error);
        });
    });
}