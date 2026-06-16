
/* ==========================
   ELEMENTS
========================== */

const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message");
const sendBtn = document.getElementById("send-btn");
const voiceBtn = document.getElementById("voice-btn");
const typingIndicator = document.getElementById("typing-indicator");
const themeToggle = document.getElementById("theme-toggle");
const languageSelect = document.getElementById("language-select");

/* ==========================
   DARK MODE
========================== */

if(localStorage.getItem("theme") === "dark"){
    document.body.classList.add("dark");
}

window.addEventListener("DOMContentLoaded", () => {

    /* Theme Toggle */

    if(themeToggle){

        if(document.body.classList.contains("dark")){
            themeToggle.innerHTML = "☀️ Light Mode";
        }else{
            themeToggle.innerHTML = "🌙 Dark Mode";
        }

        themeToggle.addEventListener("click", () => {

            document.body.classList.toggle("dark");

            if(document.body.classList.contains("dark")){

                localStorage.setItem("theme", "dark");
                themeToggle.innerHTML = "☀️ Light Mode";

            }else{

                localStorage.setItem("theme", "light");
                themeToggle.innerHTML = "🌙 Dark Mode";

            }

        });

    }

    /* Suggestion Chips */

    const suggestionChips =
    document.querySelectorAll(".suggestion-chip");

    suggestionChips.forEach(chip => {

        chip.addEventListener("click", () => {

            if(!messageInput) return;

            messageInput.value =
            chip.textContent.trim();

            sendMessage();

        });

    });

});

/* ==========================
   CHAT FUNCTIONS
========================== */

function addUserMessage(message){

    if(!chatBox) return;

    const div = document.createElement("div");

    div.className = "user-message";

    div.innerHTML = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function addBotMessage(message){

    if(!chatBox) return;

    const div = document.createElement("div");

    div.className = "bot-message";

    div.innerHTML =
    message.replace(/\n/g,"<br>");

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage(){

    if(!messageInput) return;

    const message =
    messageInput.value.trim();

    if(message === ""){
        return;
    }

    addUserMessage(message);

    messageInput.value = "";

    if(typingIndicator){
        typingIndicator.style.display = "block";
    }

    try{

        const response =
        await fetch("/chat",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                message:message,

                language:
                languageSelect
                ? languageSelect.value
                : "English"

            })

        });

        const data =
        await response.json();

        if(typingIndicator){
            typingIndicator.style.display = "none";
        }

        addBotMessage(data.response);

    }
    catch(error){

        if(typingIndicator){
            typingIndicator.style.display = "none";
        }

        addBotMessage(
            "❌ Unable to connect to server."
        );

        console.error(error);
    }

}

/* ==========================
   SEND BUTTON
========================== */

if(sendBtn){

    sendBtn.addEventListener(
        "click",
        sendMessage
    );

}

/* ==========================
   ENTER KEY
========================== */

if(messageInput){

    messageInput.addEventListener(
        "keypress",
        function(e){

            if(e.key === "Enter"){
                sendMessage();
            }

        }
    );

}

/* ==========================
   VOICE INPUT
========================== */

if(
    voiceBtn &&
    "webkitSpeechRecognition" in window
){

    const recognition =
    new webkitSpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    voiceBtn.addEventListener(
        "click",
        () => {

            recognition.start();

            voiceBtn.innerHTML =
            "🎙 Listening...";

        }
    );

    recognition.onresult =
    function(event){

        const transcript =
        event.results[0][0].transcript;

        if(messageInput){

            messageInput.value =
            transcript;

        }

        voiceBtn.innerHTML = "🎤";
    };

    recognition.onerror =
    function(){

        voiceBtn.innerHTML = "🎤";

    };

    recognition.onend =
    function(){

        voiceBtn.innerHTML = "🎤";

    };

}

/* ==========================
   WEATHER
========================== */

const weatherBtn =
document.getElementById("weather-btn");

if(weatherBtn){

    weatherBtn.addEventListener(
        "click",
        async () => {

            const cityInput =
            document.getElementById("city");

            const result =
            document.getElementById(
                "weather-result"
            );

            if(!cityInput) return;

            const city =
            cityInput.value.trim();

            if(city === ""){
                return;
            }

            try{

                const response =
                await fetch(
                `/weather?city=${city}`
                );

                const data =
                await response.json();

                if(data.success){

                    result.innerHTML = `

                    <div class="weather-card">

                        <h3>
                        📍 ${data.city},
                        ${data.country}
                        </h3>

                        <p>
                        🌡 Temperature:
                        ${data.temperature}°C
                        </p>

                        <p>
                        💧 Humidity:
                        ${data.humidity}%
                        </p>

                        <p>
                        🌤 Weather:
                        ${data.weather}
                        </p>

                        <p>
                        💨 Wind Speed:
                        ${data.wind_speed} m/s
                        </p>

                    </div>

                    `;

                }else{

                    result.innerHTML =
                    `<p>${data.message}</p>`;

                }

            }
            catch(error){

                console.error(error);

                result.innerHTML =
                "<p>❌ Weather service unavailable.</p>";

            }

        }
    );

}
