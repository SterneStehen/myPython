import openai
import time

# Установите ваш ключ доступа
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Выберите движок, например, text-davinci-003
        prompt=prompt,
        max_tokens=50,  # Максимальное количество токенов в ответе
        n=1,  # Количество ответов, которые вы хотите получить
        stop=None,  # Остановочные фразы, чтобы указать конец ответа (необязательно)
        temperature=0.7,  # Параметр, который контролирует "творчество" ответа (чем выше, тем более разнообразные ответы)
        top_p=1.0,  # Отсечение модели, чтобы сгенерировать ответы только из наиболее вероятных токенов
        frequency_penalty=0.0,  # Чем выше, тем более повторяющиеся ответы будут уменьшаться
        presence_penalty=0.0  # Чем выше, тем более модель будет учитывать предыдущий контекст
    )
    return response.choices[0].text.strip()

# Пример использования
while True:
    user_input = input("Вы: ")
    if user_input.lower() == 'q':
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT: " + response)
    time.sleep(2)