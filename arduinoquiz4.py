import time

# Arduino quiz questions
arduino_questions = [
    {"question": "What is the maximum voltage output of an Arduino digital pin?", "options": ["3.3V", "5V", "9V", "12V"], "answer": "5V"},
    {"question": "Which function is used to initialize the Serial communication?", "options": ["Serial.setup()", "Serial.begin()", "Serial.init()", "Serial.start()"], "answer": "Serial.begin()"},
    {"question": "Which Arduino board is best suited for large I/O pin requirements?", "options": ["Arduino Uno", "Arduino Nano", "Arduino Mega", "Arduino Due"], "answer": "Arduino Mega"},
    {"question": "What does the 'void setup()' function in Arduino do?", "options": ["Runs once at the start", "Runs continuously", "Initializes pins", "Cleans up memory"], "answer": "Runs once at the start"},
    {"question": "Which of these is NOT a valid Arduino data type?", "options": ["int", "float", "void", "decimal"], "answer": "decimal"},
    {"question": "How much flash memory does an Arduino Uno have?", "options": ["32 KB", "64 KB", "16 KB", "128 KB"], "answer": "32 KB"},
    {"question": "What is the correct way to read an analog value from pin A0?", "options": ["analogRead(A0)", "digitalRead(A0)", "readAnalog(A0)", "analogInput(A0)"], "answer": "analogRead(A0)"},
    {"question": "Which function is used to delay the execution of the Arduino code?", "options": ["wait()", "delay()", "pause()", "sleep()"], "answer": "delay()"},
    {"question": "Which communication protocol is NOT natively supported by Arduino?", "options": ["SPI", "I2C", "UART", "USB-C"], "answer": "USB-C"},
    {"question": "How do you set a pin as an output in Arduino?", "options": ["pinMode(pin, OUTPUT)", "digitalWrite(pin, OUTPUT)", "setPin(pin, OUT)", "outputMode(pin, OUTPUT)"], "answer": "pinMode(pin, OUTPUT)"},
    {"question": "What is the operating voltage of the Arduino Uno?", "options": ["3.3V", "5V", "9V", "12V"], "answer": "5V"},
    {"question": "Which function is used to write a high or low value to a digital pin?", "options": ["digitalWrite()", "analogWrite()", "pinWrite()", "setPinValue()"], "answer": "digitalWrite()"},
    {"question": "Which sensor can be used to detect temperature?", "options": ["DHT11", "LDR", "IR sensor", "Flame sensor"], "answer": "DHT11"},
    {"question": "What is the purpose of a pull-up resistor?", "options": ["To ensure a default high signal", "To ensure a default low signal", "To increase voltage", "To decrease current"], "answer": "To ensure a default high signal"},
    {"question": "Which function generates a PWM signal on a pin?", "options": ["analogWrite()", "digitalWrite()", "pwmWrite()", "writePWM()"], "answer": "analogWrite()"},
    {"question": "Which of these commands initializes the LCD screen in Arduino?", "options": ["lcd.begin()", "lcd.init()", "lcd.start()", "lcd.setup()"], "answer": "lcd.begin()"},
    {"question": "How many interrupt pins does an Arduino Uno have?", "options": ["2", "4", "6", "8"], "answer": "2"},
    {"question": "Which of these protocols is typically used with an RFID reader?", "options": ["I2C", "SPI", "UART", "RF"], "answer": "UART"},
    {"question": "Which sensor is used to detect the presence of light?", "options": ["LDR", "DHT11", "Flame sensor", "IR sensor"], "answer": "LDR"},
    {"question": "What is the output voltage of an Arduino Uno's 3.3V pin?", "options": ["3.3V", "5V", "9V", "12V"], "answer": "3.3V"},
    {"question": "Which function ends serial communication in Arduino?", "options": ["Serial.end()", "Serial.close()", "Serial.stop()", "Serial.terminate()"], "answer": "Serial.end()"},
    {"question": "How many analog input pins does the Arduino Uno have?", "options": ["6", "8", "10", "12"], "answer": "6"},
    {"question": "Which Arduino function is used to attach a servo motor?", "options": ["servo.attach()", "servo.connect()", "motor.attach()", "servo.init()"], "answer": "servo.attach()"},
    {"question": "Which library is used to interface with an OLED display?", "options": ["Adafruit_SSD1306", "Wire.h", "Servo.h", "LiquidCrystal.h"], "answer": "Adafruit_SSD1306"},
    {"question": "How do you set the baud rate for serial communication?", "options": ["Serial.begin(9600)", "Serial.baud(9600)", "Serial.setBaud(9600)", "Serial.config(9600)"], "answer": "Serial.begin(9600)"},
    {"question": "What is the default voltage reference for analogRead in Arduino?", "options": ["5V", "3.3V", "1.1V", "2.5V"], "answer": "5V"},
    {"question": "Which command is used to initialize the I2C protocol in Arduino?", "options": ["Wire.begin()", "I2C.begin()", "Wire.init()", "I2C.start()"], "answer": "Wire.begin()"},
    {"question": "How do you define a pin as an input in Arduino?", "options": ["pinMode(pin, INPUT)", "digitalRead(pin)", "setPin(pin, IN)", "inputMode(pin, IN)"], "answer": "pinMode(pin, INPUT)"},
    {"question": "Which type of motor allows for precise control of angular position?", "options": ["Servo motor", "DC motor", "Stepper motor", "AC motor"], "answer": "Stepper motor"},
    {"question": "What does the analogWrite() function do in Arduino?", "options": ["Generates a PWM signal", "Writes a digital HIGH", "Writes an analog value", "Generates a digital signal"], "answer": "Generates a PWM signal"}
]

# Arduino quiz game
def arduino_quiz():
    score = 0
    for q in arduino_questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        while True:
            answer = input("Enter the number of your answer: ").strip()
            if answer.isdigit() and 1 <= int(answer) <= len(q["options"]):
                if q["options"][int(answer) - 1] == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {q['answer']}.")
                break
            else:
                print("Invalid input, please choose a valid option.")

    print(f"\nYour final score is {score} out of {len(arduino_questions)}.")
    input("Press Enter to exit...")  # Keep the console open

arduino_quiz()
