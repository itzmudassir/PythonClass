import random
import time

# Arduino quiz questions
arduino_questions = [
    {"question": "What will happen if you write pinMode(A0, OUTPUT); on an Arduino Uno?", 
     "options": ["A0 will be configured as a digital output", "A0 will be configured as an analog output", 
                 "A0 will read analog values", "The code will raise a compile error"], 
     "answer": "A0 will be configured as a digital output"},
    
    {"question": "Which of the following commands will generate a PWM signal with a 50% duty cycle on pin 9?", 
     "options": ["analogWrite(9, 127);", "analogWrite(9, 255);", "digitalWrite(9, HIGH);", 
                 "pwmWrite(9, 1023);"], 
     "answer": "analogWrite(9, 127);"},
    
    {"question": "How does millis() behave after approximately 50 days of continuous running?", 
     "options": ["It resets to 0", "It stops working", "It continues normally", "It generates a negative value"], 
     "answer": "It resets to 0"},
    
    {"question": "What is the main difference between attachInterrupt() and detachInterrupt() functions?", 
     "options": ["attachInterrupt() links an interrupt to a pin, while detachInterrupt() disables it", 
                 "attachInterrupt() stops the program, while detachInterrupt() continues it", 
                 "attachInterrupt() is used for analog pins, detachInterrupt() for digital pins", 
                 "attachInterrupt() pauses execution, detachInterrupt() resumes execution"], 
     "answer": "attachInterrupt() links an interrupt to a pin, while detachInterrupt() disables it"},
    
    {"question": "What will happen if you call digitalWrite(13, HIGH); before calling pinMode(13, OUTPUT);?", 
     "options": ["The pin will be set to HIGH", "The code will compile but not work properly", 
                 "The code will not compile", "The code will throw a runtime error"], 
     "answer": "The pin will be set to HIGH"},
    
    {"question": "Which function is used to disable interrupts globally in Arduino?", 
     "options": ["noInterrupts();", "disableInterrupts();", "interrupts(OFF);", "detachInterrupt();"], 
     "answer": "noInterrupts();"},
    
    {"question": "How can you measure the duration of a HIGH pulse using Arduino?", 
     "options": ["pulseIn(pin, HIGH);", "pulseDuration(pin);", "measurePulse(pin, HIGH);", 
                 "readHighTime(pin);"], 
     "answer": "pulseIn(pin, HIGH);"},
    
    {"question": "What is the function of F() macro in Arduino?", 
     "options": ["To store string literals in flash memory instead of SRAM", 
                 "To convert integers to float", "To store floats as integers", 
                 "To format strings"], 
     "answer": "To store string literals in flash memory instead of SRAM"},
    
    {"question": "What will be the value of millis() after 60 seconds of Arduino running?", 
     "options": ["60000", "6000", "60", "65535"], 
     "answer": "60000"},
    
    {"question": "Which of the following commands will output a 1kHz square wave on pin 9 using a timer?", 
     "options": ["Use a timer library to manipulate pin 9", "analogWrite(9, 500);", 
                 "digitalWrite(9, HIGH);", "pwmWrite(9, 1);"], 
     "answer": "Use a timer library to manipulate pin 9"},
    
    {"question": "What happens when you exceed the maximum current of an Arduino pin (40mA)?", 
     "options": ["The microcontroller can be permanently damaged", "It will trigger an automatic reset", 
                 "It will shut down the pin only", "Nothing will happen"], 
     "answer": "The microcontroller can be permanently damaged"},
    
    {"question": "What will the following code do: digitalWrite(7, analogRead(A0));?", 
     "options": ["Set pin 7 to HIGH if analogRead(A0) > 512", "Set pin 7 to LOW if analogRead(A0) < 512", 
                 "Generate a compile error", "It converts analogRead to a digitalWrite and sets the value"], 
     "answer": "Generate a compile error"},
    
    {"question": "Which command will continuously send a PWM signal to a pin until changed?", 
     "options": ["analogWrite()", "pwmWrite()", "digitalWrite()", "pulseWrite()"], 
     "answer": "analogWrite()"},
    
    {"question": "What happens if you try to perform analogRead(13) on a digital pin?", 
     "options": ["You get unpredictable values", "It will read HIGH or LOW", "The program will crash", 
                 "It generates a compile-time error"], 
     "answer": "You get unpredictable values"},
    
    {"question": "What does the following command do: TCCR1A = 0x00;?", 
     "options": ["Sets timer 1 configuration to normal mode", "Resets timer 1", 
                 "Disables timer 1", "Enables timer 1 in fast PWM mode"], 
     "answer": "Sets timer 1 configuration to normal mode"},
    
    {"question": "What is the function of EEPROM.update() in Arduino?", 
     "options": ["It writes only if the value is different to avoid unnecessary writes", 
                 "It updates an EEPROM address to the next available one", 
                 "It resets the EEPROM data", "It reads from the EEPROM"], 
     "answer": "It writes only if the value is different to avoid unnecessary writes"},
    
    {"question": "What will happen if you set the baud rate incorrectly in Serial.begin()?", 
     "options": ["Serial data will be gibberish", "It will work but slower", 
                 "Serial communication will automatically adjust", 
                 "The program will stop running"], 
     "answer": "Serial data will be gibberish"},
    
    {"question": "Which Arduino pin can generate PWM on a Mega but not on an Uno?", 
     "options": ["Pin 44", "Pin 9", "Pin 13", "Pin 7"], 
     "answer": "Pin 44"},
    
    {"question": "How do you manipulate individual bits in a register such as PORTB?", 
     "options": ["Using bitwise operators like | and &", "By writing to a bit position", 
                 "Using the registerBit() function", "Using pinMode() and digitalWrite()"], 
     "answer": "Using bitwise operators like | and &"},
    
    {"question": "Which command will restart the Arduino using software?", 
     "options": ["There is no software reset command in Arduino", "resetArduino();", 
                 "Serial.reset();", "reset();"], 
     "answer": "There is no software reset command in Arduino"},
    
    {"question": "How does analogReference(INTERNAL) affect analogRead() on an Arduino Uno?", 
     "options": ["It changes the reference voltage to 1.1V", "It changes the reference voltage to 5V", 
                 "It changes the reference voltage to 3.3V", "It resets the analog pins"], 
     "answer": "It changes the reference voltage to 1.1V"},
    
    {"question": "What will shiftOut(dataPin, clockPin, MSBFIRST, 0b10101010); do?", 
     "options": ["Send bits starting from the most significant bit (10101010)", 
                 "Send bits starting from the least significant bit (01010101)", 
                 "Set the clockPin HIGH and dataPin LOW", "Generate a clock pulse"], 
     "answer": "Send bits starting from the most significant bit (10101010)"},
    
    {"question": "What will happen if you initialize a pin with pinMode(13, INPUT_PULLUP);?", 
     "options": ["Pin 13 will have an internal pull-up resistor", "Pin 13 will output HIGH", 
                 "Pin 13 will output LOW", "Pin 13 will read analog values"], 
     "answer": "Pin 13 will have an internal pull-up resistor"},
    
    {"question": "What is the maximum memory available for storing variables on an Arduino Uno?", 
     "options": ["2KB SRAM", "32KB Flash", "8KB EEPROM", "4KB SRAM"], 
     "answer": "2KB SRAM"},
    
    {"question": "What does SPI.setClockDivider(SPI_CLOCK_DIV16); do?", 
     "options": ["Sets the SPI clock speed to 1/16 of the Arduino system clock", 
                 "Multiplies the clock speed by 16", 
                 "Sets the clock speed to 16Hz", 
                 "Stops the SPI clock"], 
     "answer": "Sets the SPI clock speed to 1/16 of the Arduino system clock"},
    
    
    {"question": "Which command is used to send a byte of data through I2C in Arduino?", 
     "options": ["Wire.write()", "Serial.write()", "Wire.send()", "I2C.write()"], 
     "answer": "Wire.write()"},
    
    {"question": "What happens if you use delayMicroseconds(1); in your Arduino sketch?", 
     "options": ["Pauses the program for approximately 1 microsecond", 
                 "Pauses the program for 1 millisecond", 
                 "Pauses the program for 1000 microseconds", 
                 "The command is not supported in Arduino"], 
     "answer": "Pauses the program for approximately 1 microsecond"},
    
    {"question": "What is the result of Serial.print(3/2); on an Arduino?", 
     "options": ["1", "1.5", "2", "It will cause a compile error"], 
     "answer": "1"},
    
    {"question": "What does cli() function do in Arduino?", 
     "options": ["Disables all interrupts", 
                 "Clears the serial input buffer", 
                 "Clears the I/O registers", 
                 "Resets the microcontroller"], 
     "answer": "Disables all interrupts"},
    
    {"question": "What is the purpose of the sei() function in Arduino?", 
     "options": ["Enables interrupts globally", 
                 "Enables the serial communication", 
                 "Enables the digital I/O pins", 
                 "Sets the SPI interface to master mode"], 
     "answer": "Enables interrupts globally"},
    
    {"question": "What is the effect of writing analogWrite(pin, 0); to a PWM pin?", 
     "options": ["It sets the output to 0V (LOW)", "It turns the pin off", 
                 "It sets the output to 255", "It has no effect"], 
     "answer": "It sets the output to 0V (LOW)"},
    
    {"question": "Which of the following is not a correct way to declare an array in Arduino?", 
     "options": ["int myArray[5];", "byte arr[10] = {0};", "char arr[3] = {0, 1};", 
                 "float myArray[] = {1.2, 2.3, 3.4};"], 
     "answer": "char arr[3] = {0, 1};"},
    
    {"question": "What is the purpose of watchdog timer in Arduino?", 
     "options": ["To reset the microcontroller if the code hangs", 
                 "To track elapsed time between events", 
                 "To monitor power consumption", 
                 "To enable low-power mode"], 
     "answer": "To reset the microcontroller if the code hangs"},
    
    {"question": "What is the return type of random() function in Arduino?", 
     "options": ["long", "int", "float", "byte"], 
     "answer": "long"},
    
    {"question": "What will pinMode(13, INPUT); do?", 
     "options": ["Configure pin 13 as an input", "Set pin 13 to LOW", 
                 "Read the analog value on pin 13", "It will throw an error"], 
     "answer": "Configure pin 13 as an input"}
]



# Arduino quiz game
def arduino_quiz():
    score = 0
    for q in arduino_questions:
        print("\n" + q["question"])
        
        # Shuffle options while keeping track of the correct answer
        options = q["options"][:]
        random.shuffle(options)
        correct_answer_index = options.index(q["answer"])
        
        # Display options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        # Get user's answer
        while True:
            answer = input("Enter the number of your answer: ").strip()
            if answer.isdigit() and 1 <= int(answer) <= len(options):
                if int(answer) - 1 == correct_answer_index:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is: {q['answer']}")
                break
            else:
                print("Invalid input. Please enter a valid option number.")
    
    # Display final score
    print(f"\nYour final score is {score}/{len(arduino_questions)}.")
    
# Start the quiz
arduino_quiz()
