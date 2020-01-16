"""
This is multi-language commands list in order to use for visionRecog.py, 
vision_recog_with_hotword.py and vision_recog_with_button.py.
This file contains the versions of English, Spanish and Japanese, 
but you can edit and add commands in other languages by adding the following dictionary.

"""

words_dict = {
    'en':
    {
    'talk_start_button':
    'Push the button and say comands. "What is this?", "Can you read this?" or "What logo is this?"',
    'command_list':
    'List of valid commands',
    'waiting_button':
    'Waiting to push the button...',
    'waiting_hotword':
    'Waiting to hear the hotword',
    'waiting_command':
    'Waiting to hear the command...',
    'talk_sorry':
    'I\'m sorry. Please try to say again.',
    'your_command':
    'Your command...',
    'finish_list':
        ['thanks',
         'thank you',
         'goodbye'],
    'talk_finish':
    'program ended',
    'read_text':
    ['can you read this',
    'can you read that'],
    'read_logo':
    ["what logo is this",
    "what logo is that"],
    'not_logo':
    'Sorry I don\'t know that logo',
    'label_detect':
    ["what is this",
    "what is that"],
    'talk_again':
    'I \'m sorry. I cannot hear you well. Please repeat again.',
    'text_loaded':
    'Text loaded is as follows:',
    'text_original':
    'Following is the original text:',
    'text_resulted':
    'Following is the translated result:'
    },
    'es':
    {
    'talk_start_button':
    'Presione el botón y diga comandos. "¿Qué es esto?", "¿Puedes leer esto?" o "¿Qué logo es este?" ',
    'command_list':
    'Lista de comandos válidos',
    'waiting_button':
    'Esperando para presionar el botón ...',
    'waiting_hotword':
    'Esperando escuchar la palabra clave',
    'waiting_command':
    'Esperando escuchar la orden ...',
    'talk_sorry':
    'Lo siento. Por favor, intente decirlo de nuevo.',
    'your_command':
    'Tu orden ...',
    'finish_list':
        ['gracias',
         'muchas gracias',
         'adiós',
         'hasta luego'],
    'talk_finish':
    'programa finalizado',
    'read_text':
     ['puedes leer esto',
         'puedes leer este texto'],
    'read_logo':
    ['qué logo es este',
     'Conoces este logo',],
    'not_logo':
    'Lo siento mucho, pero no conozco este logo.',
    'label_detect':
    ['qué es esto',
    'qué es'],
    'talk_again':
    'Lo siento. No puedo oirle bien. Por favor, repita de nuevo.',
    'text_loaded':
    'El texto cargado es el siguiente:',
    'text_original':
    'El siguiente es el texto original:',
    'text_resulted':
    'A continuación se muestra el resultado traducido:'
    },
    'ja':
    {
    'talk_start_button':
    'ボタンを押して、「これは何ですか」「これは何と読みますか」\n「このロゴは何ですか」などのコマンドを言ってください',
    'command_list':
    '有効なコマンド一覧',
    'waiting_button':
    'ボタンが押されるのを待っています...',
    'waiting_hotword':
    'ホットワードを聞き取り中...',
    'waiting_command':
    'コマンドを聞き取り中...',
    'talk_sorry':
    '申し訳ございません。もう一度言ってください',
    'your_command':
    'あなたのコマンド',
    'finish_list':
        ['終',
        '終了',
        '終わり',
        'さようなら',
        'さよなら',
        'ありがとう'],
    'talk_finish':
    'プログラムを終了しました',
    'read_text':
    ['これは何と読みますか',
        'この文章は何ですか',
        'この文を読んで'],
    'read_logo':
    ["このロゴは何ですか",
    "このロゴを知ってますか"],
    'not_logo':
    '申し訳ございませんが、そのロゴは分かりません',
    'label_detect':
    ["これは何ですか",
    "あれは何ですか"],
    'talk_again':
    'うまく聞き取れませんでした。もう一度おっしゃってください',
    'text_loaded':
    '読み取った文章は、以下のとおりです',
    'text_original':
    '原文での表示結果は、以下のとおりです',
    'text_resulted':
    '結果は以下のとおりです。'
    }
}