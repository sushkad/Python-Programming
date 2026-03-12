class Animal:
    def sound(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"

# Example usage
dog = Dog()
cat = Cat()

print(f"Dog: {dog.sound()}")
print(f"Cat: {cat.sound()}")