#!/bin/bash

saving_data() {
    local TEXT="$1"
    local VOICE="$2"
    local LANGUAGE="$3"
    local ACCENT="$4"
    local TON="$5"
    local FORMAT="$6"

    echo "Texto: $TEXT | Gênero: $VOICE | Linguagem: $LANGUAGE | Sotaque: $ACCENT | Tonalidade: $TON | Formato: $FORMAT" 
}

export -f saving_data

yad --title="Simple Linux TTS" \
 --form \
 --field="Texto que será narrado" ""\
 --field="Voz:CB" "Homem!Mulher"\
 --field="Language:CB" "English" \
 --field="Sotaque:CB" "Britanico" \
 --field="Tonalização:TXT" "" \
 --field="Ouvir:BTN" "" \
 --field="Formatos:CB" "MP3!WAV" \
 --field="Salva:BTN" 'bash -c "saving_data %1 %2 %3 %4 %5 %7"'
