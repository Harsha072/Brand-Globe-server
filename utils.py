import openai  

def generate_description(brand_name):
        input_text = f"Generate a product description for the brand '{brand_name}' in four lines only."

        try:
            # Generate product description using OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": input_text}],
                max_tokens=70
            )
            generated_description = response.choices[0].message['content']
            print(generated_description)
            return generated_description
        except Exception as e:
            print(f"Error generating content: {e}")
            return None