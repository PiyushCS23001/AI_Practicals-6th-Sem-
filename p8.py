isa = {
  "bird":"animal",
  "dog":"animal",
  "sparrow":"bird",
}

has_a = {
  "animal" : ["cells"],
  "bird" : ["wings"],
  "dog" : ["tail"],
}

can_do = {
  "bird" : ["fly"],
  "dog": ["bark"],
}

def get_superclass(concept):
    return isa.get(concept, None)

def inherits_property(concept, property_name):
    if concept in has_a and property_name in has_a[concept]:
        return True
   
    parent = get_superclass(concept)
    if parent:
        return inherits_property(parent, property_name)
   
    return False

def inherits_ability(concept, ability_name):
    if concept in can_do and ability_name in can_do[concept]:
        return True
   
    parent = get_superclass(concept)
    if parent:
        return inherits_ability(parent, ability_name)
   
    return False

print("sparrow has wings:", inherits_property("sparrow","wings"))
print("dog has wings:", inherits_property("dog","wings"))
print("dog has tail:", inherits_property("dog","tail"))

print("sparrow can fly:", inherits_ability("sparrow","fly"))
print("dog can fly:", inherits_ability("dog","fly"))
print("dog can bark:", inherits_ability("dog","bark"))