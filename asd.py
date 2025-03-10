import streamlit as st
import streamlit.components.v1 as components

# App title
st.title("NIHSS Калкулатор")

# HTML content embedded directly in the Python script
html_content = """<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NIHSS Калкулатор</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .category {
            margin-bottom: 30px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .category h2 {
            margin-top: 0;
            color: #3498db;
            font-size: 1.2em;
        }
        .question {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #fff;
        }
        #result {
            margin-top: 20px;
            padding: 15px;
            background-color: #e8f4fd;
            border-radius: 5px;
            text-align: center;
            font-size: 1.2em;
            font-weight: bold;
        }
        .results-container {
            margin-top: 20px;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }
        .severity {
            margin-top: 10px;
            font-weight: bold;
        }
        .severity-mild {
            color: #27ae60;
        }
        .severity-moderate {
            color: #f39c12;
        }
        .severity-moderate-severe {
            color: #e67e22;
        }
        .severity-severe {
            color: #c0392b;
        }
        button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1em;
            cursor: pointer;
            margin-top: 20px;
        }
        button:hover {
            background-color: #2980b9;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            font-size: 0.8em;
            color: #7f8c8d;
        }
        @media print {
            .no-print {
                display: none;
            }
            body, .container {
                background-color: white;
                box-shadow: none;
            }
            .category {
                break-inside: avoid;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>NIHSS Калкулатор</h1>
        <p>Национална скала за мозочен удар на Институтите за здравје (NIHSS)</p>
        
        <form id="nihssForm">
            <!-- 1. Ниво на свест -->
            <div class="category">
                <h2>1. Ниво на свест</h2>
                
                <div class="question">
                    <label for="consciousness">1a. Ниво на свест</label>
                    <select id="consciousness" name="consciousness">
                        <option value="0">0 = Целосно буден</option>
                        <option value="1">1 = Поспан</option>
                        <option value="2">2 = Сомнолентен</option>
                        <option value="3">3 = Кома/не реагира</option>
                    </select>
                </div>
                
                <div class="question">
                    <label for="consciousnessQuestions">1b. Прашања за ниво на свест</label>
                    <select id="consciousnessQuestions" name="consciousnessQuestions">
                        <option value="0">0 = Одговара на двете прашања точно</option>
                        <option value="1">1 = Одговара точно на едно прашање</option>
                        <option value="2">2 = Не одговара точно на ниту едно прашање</option>
                    </select>
                </div>
                
                <div class="question">
                    <label for="consciousnessCommands">1c. Команди за ниво на свест</label>
                    <select id="consciousnessCommands" name="consciousnessCommands">
                        <option value="0">0 = Извршува обете команди правилно</option>
                        <option value="1">1 = Извршува една команда правилно</option>
                        <option value="2">2 = Не извршува ниту една команда правилно</option>
                    </select>
                </div>
            </div>
            
            <!-- 2. Движење на очите -->
            <div class="category">
                <h2>2. Движење на очите</h2>
                <div class="question">
                    <label for="bestGaze">Најдобар поглед</label>
                    <select id="bestGaze" name="bestGaze">
                        <option value="0">0 = Нормално</option>
                        <option value="1">1 = Парцијална пареза на погледот</option>
                        <option value="2">2 = Присилна девијација или тотална пареза на погледот</option>
                    </select>
                </div>
            </div>
            
            <!-- 3. Видно поле -->
            <div class="category">
                <h2>3. Видно поле</h2>
                <div class="question">
                    <label for="visualFields">Проценка на видното поле</label>
                    <select id="visualFields" name="visualFields">
                        <option value="0">0 = Без губење на видот</option>
                        <option value="1">1 = Парцијална хемианопсија</option>
                        <option value="2">2 = Комплетна хемианопсија</option>
                        <option value="3">3 = Билатерална хемианопсија</option>
                    </select>
                </div>
            </div>
            
            <!-- 4. Фацијална пареза -->
            <div class="category">
                <h2>4. Фацијална пареза</h2>
                <div class="question">
                    <label for="facialPalsy">Движења на лицето</label>
                    <select id="facialPalsy" name="facialPalsy">
                        <option value="0">0 = Нормални симетрични движења</option>
                        <option value="1">1 = Минорна парализа</option>
                        <option value="2">2 = Парцијална парализа</option>
                        <option value="3">3 = Комплетна парализа на едната или двете страни</option>
                    </select>
                </div>
            </div>
            
            <!-- 5. Моторна функција - Рака -->
            <div class="category">
                <h2>5. Моторна функција - Рака</h2>
                
                <div class="question">
                    <label for="motorLeft">5a. Лева рака</label>
                    <select id="motorLeft" name="motorLeft">
                        <option value="0">0 = Нема пропаѓање</option>
                        <option value="1">1 = Пропаѓање пред 10 секунди</option>
                        <option value="2">2 = Некаков напор против гравитација</option>
                        <option value="3">3 = Нема напор против гравитација</option>
                        <option value="4">4 = Нема движење</option>
                        <option value="UN">UN = Ампутација или фузија на зглоб</option>
                    </select>
                </div>
                
                <div class="question">
                    <label for="motorRight">5b. Десна рака</label>
                    <select id="motorRight" name="motorRight">
                        <option value="0">0 = Нема пропаѓање</option>
                        <option value="1">1 = Пропаѓање пред 10 секунди</option>
                        <option value="2">2 = Некаков напор против гравитација</option>
                        <option value="3">3 = Нема напор против гравитација</option>
                        <option value="4">4 = Нема движење</option>
                        <option value="UN">UN = Ампутација или фузија на зглоб</option>
                    </select>
                </div>
            </div>
            
            <!-- 6. Моторна функција - Нога -->
            <div class="category">
                <h2>6. Моторна функција - Нога</h2>
                
                <div class="question">
                    <label for="motorLegLeft">6a. Лева нога</label>
                    <select id="motorLegLeft" name="motorLegLeft">
                        <option value="0">0 = Нема пропаѓање</option>
                        <option value="1">1 = Пропаѓање пред 5 секунди</option>
                        <option value="2">2 = Некаков напор против гравитација</option>
                        <option value="3">3 = Нема напор против гравитација</option>
                        <option value="4">4 = Нема движење</option>
                        <option value="UN">UN = Ампутација или фузија на зглоб</option>
                    </select>
                </div>
                
                <div class="question">
                    <label for="motorLegRight">6b. Десна нога</label>
                    <select id="motorLegRight" name="motorLegRight">
                        <option value="0">0 = Нема пропаѓање</option>
                        <option value="1">1 = Пропаѓање пред 5 секунди</option>
                        <option value="2">2 = Некаков напор против гравитација</option>
                        <option value="3">3 = Нема напор против гравитација</option>
                        <option value="4">4 = Нема движење</option>
                        <option value="UN">UN = Ампутација или фузија на зглоб</option>
                    </select>
                </div>
            </div>
            
            <!-- 7. Атаксија на екстремитети -->
            <div class="category">
                <h2>7. Атаксија на екстремитети</h2>
                <div class="question">
                    <label for="limbAtaxia">Координација на движењата</label>
                    <select id="limbAtaxia" name="limbAtaxia">
                        <option value="0">0 = Отсутна</option>
                        <option value="1">1 = Присутна во една рака или нога</option>
                        <option value="2">2 = Присутна во рака и нога</option>
                        <option value="UN">UN = Ампутација или фузија на зглоб</option>
                    </select>
                </div>
            </div>
            
            <!-- 8. Сензитивност -->
            <div class="category">
                <h2>8. Сензитивност</h2>
                <div class="question">
                    <label for="sensory">Чувство на убод со игла</label>
                    <select id="sensory" name="sensory">
                        <option value="0">0 = Нормално</option>
                        <option value="1">1 = Блага до умерена сензорна загуба</option>
                        <option value="2">2 = Тешка или тотална сензорна загуба</option>
                    </select>
                </div>
            </div>
            
            <!-- 9. Најдобар јазик -->
            <div class="category">
                <h2>9. Најдобар јазик</h2>
                <div class="question">
                    <label for="bestLanguage">Способност за зборување и разбирање</label>
                    <select id="bestLanguage" name="bestLanguage">
                        <option value="0">0 = Нема афазија</option>
                        <option value="1">1 = Блага до умерена афазија</option>
                        <option value="2">2 = Тешка афазија</option>
                        <option value="3">3 = Нем</option>
                    </select>
                </div>
            </div>
            
            <!-- 10. Дизартрија -->
            <div class="category">
                <h2>10. Дизартрија</h2>
                <div class="question">
                    <label for="dysarthria">Јасност на говорот</label>
                    <select id="dysarthria" name="dysarthria">
                        <option value="0">0 = Нормален</option>
                        <option value="1">1 = Блага до умерена</option>
                        <option value="2">2 = Тешка</option>
                        <option value="UN">UN = Интубиран или друга физичка бариера</option>
                    </select>
                </div>
            </div>
            
            <!-- 11. Негирање/Невнимание -->
            <div class="category">
                <h2>11. Негирање/Невнимание</h2>
                <div class="question">
                    <label for="extinction">Препознавање</label>
                    <select id="extinction" name="extinction">
                        <option value="0">0 = Нема абнормалност</option>
                        <option value="1">1 = Невнимание на еден сензорен модалитет</option>
                        <option value="2">2 = Тешко хеми-невнимание</option>
                    </select>
                </div>
            </div>
            
            <button type="button" onclick="calculateNIHSS()">Пресметај NIHSS скор</button>
        </form>
        
        <div class="results-container">
            <div id="result">Вкупен NIHSS скор: 0</div>
            <div id="severity" class="severity severity-mild">Тежина: Многу благ мозочен удар</div>
            <div id="scoreDetails"></div>
        </div>
        
        <footer class="no-print">
            <p>© 2025 NIHSS Калкулатор на македонски | Базирано на скалата на Националниот Институт за Здравје за мозочни удари</p>
        </footer>
    </div>
    
    <script>
        function calculateNIHSS() {
            const form = document.getElementById('nihssForm');
            let total = 0;
            let scoreDetails = [];
            
            // Map to hold category names in Macedonian
            const categoryNames = {
                'consciousness': '1a. Ниво на свест',
                'consciousnessQuestions': '1b. Прашања за ниво на свест',
                'consciousnessCommands': '1c. Команди за ниво на свест',
                'bestGaze': '2. Најдобар поглед',
                'visualFields': '3. Видно поле',
                'facialPalsy': '4. Фацијална пареза',
                'motorLeft': '5a. Лева рака',
                'motorRight': '5b. Десна рака',
                'motorLegLeft': '6a. Лева нога',
                'motorLegRight': '6b. Десна нога',
                'limbAtaxia': '7. Атаксија на екстремитети',
                'sensory': '8. Сензитивност',
                'bestLanguage': '9. Најдобар јазик',
                'dysarthria': '10. Дизартрија',
                'extinction': '11. Негирање/Невнимание'
            };
            
            // Process each field in the form
            for (const select of form.querySelectorAll('select')) {
                const value = select.value;
                
                // Skip fields marked as UN (untestable)
                if (value !== 'UN') {
                    const score = parseInt(value);
                    total += score;
                    scoreDetails.push(`${categoryNames[select.id]}: ${score}`);
                } else {
                    scoreDetails.push(`${categoryNames[select.id]}: Невозможно за тестирање`);
                }
            }
            
            // Update the result display
            document.getElementById('result').textContent = `Вкупен NIHSS скор: ${total}`;
            
            // Determine stroke severity based on NIHSS score
            let severityText = '';
            let severityClass = '';
            
            if (total >= 0 && total <= 4) {
                severityText = 'Тежина: Многу благ мозочен удар';
                severityClass = 'severity-mild';
            } else if (total >= 5 && total <= 15) {
                severityText = 'Тежина: Умерен мозочен удар';
                severityClass = 'severity-moderate';
            } else if (total >= 16 && total <= 20) {
                severityText = 'Тежина: Умерен до тежок мозочен удар';
                severityClass = 'severity-moderate-severe';
            } else if (total >= 21) {
                severityText = 'Тежина: Тежок мозочен удар';
                severityClass = 'severity-severe';
            }
            
            // Update severity display
            const severityElement = document.getElementById('severity');
            severityElement.textContent = severityText;
            severityElement.className = 'severity ' + severityClass;
            
            // Display score details
            document.getElementById('scoreDetails').innerHTML = `
                <h3>Детали за скорот:</h3>
                <ul>${scoreDetails.map(detail => `<li>${detail}</li>`).join('')}</ul>
                <p><strong>Интерпретација на NIHSS скорот:</strong></p>
                <ul>
                    <li>0: Нема симптоми на мозочен удар</li>
                    <li>1-4: Многу благ мозочен удар</li>
                    <li>5-15: Умерен мозочен удар</li>
                    <li>16-20: Умерен до тежок мозочен удар</li>
                    <li>21-42: Тежок мозочен удар</li>
                </ul>
            `;
        }

        // Calculate default score on page load
        document.addEventListener('DOMContentLoaded', function() {
            calculateNIHSS();
        });
    </script>
</body>
</html>"""

# Display the HTML using st.components.v1.html
components.html(html_content, height=900, scrolling=True)
