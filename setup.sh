mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"nortyneo9@yahoo.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]
base='dark'
primaryColor='#F63366'
secondaryBackgroundColor='#F0F2F6'
textColor='#FFFFFF'
font='sans serif'
" > ~/.streamlit/config.toml
