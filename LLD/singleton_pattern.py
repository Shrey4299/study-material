class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.value = value
            self.initialized = True

# Usage
singleton1 = Singleton("First Instance")
print(singleton1.value)  # Output: First Instance

singleton2 = Singleton("Second Instance")
print(singleton2.value)  # Output: First Instance

print(singleton1 is singleton2)  # Output: True


# public class Singleton {
#     // Step 1: Private static variable to hold the single instance
#     private static Singleton instance;

#     // Step 2: Private constructor to prevent instantiation
#     private Singleton() {
#         // Initialize anything necessary
#     }

#     // Step 3: Public static method to provide access to the instance
#     public static Singleton getInstance() {
#         if (instance == null) { // Lazy initialization
#             instance = new Singleton();
#         }
#         return instance;
#     }

#     // Example method
#     public void showMessage() {
#         System.out.println("Hello from the Singleton instance!");
#     }
# }

# // Usage
# class Main {
#     public static void main(String[] args) {
#         // Get the singleton instance
#         Singleton singleton = Singleton.getInstance();
#         singleton.showMessage(); // Output: Hello from the Singleton instance!

#         // Attempt to create another instance
#         Singleton anotherSingleton = Singleton.getInstance();
#         System.out.println(singleton == anotherSingleton); // Output: true
#     }
# }