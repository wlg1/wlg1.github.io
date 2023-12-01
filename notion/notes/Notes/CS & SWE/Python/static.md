# static

Static methods like .show_intro_message() don’t operate on the current instance, self, or the current class, cls. They work as independent functions enclosed in a class. You’ll typically put them inside a class when they’re closely related to that class but don’t necessarily affect the class or its instances.