from pyexpat.errors import messages


language = "Python"
version = 3.9
result= f"Я изучаю {language} версии {version}"
print(result)

text = "Hello, World"
new_text = text.replace( "Hello", "Hi")
print(new_text)

text= "apple, banana, orange"
fruits_list = text.split(",")
print(fruits_list)

text= "    Привет, мир!     "
trimmed_text= text.strip()
print(trimmed_text)

text= "Hello, World"
start_result= text.startswith("Hello")
print(start_result)
end_result= text.endswith("World")
print(end_result)

