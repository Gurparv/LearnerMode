1. [[#String]]
## String
```Java
String name = "Rohan";

name.length();
name.indexOf();
name.equals(name2);
name.trim();
```

## Arrays
```Java
int[] age = {10,15,20,25};
age.length():
int[] age2 = new int[4];

```

## ArrayLists 
```Java
ArrayList<String> names = new ArrayList <String> ();
names.add();
names.get(0);
names.set(0, "hey");
names.remove();
names.clear();
names.size();
Collections.sort(names);

for (String i : names){
	//steps
}
```

## HashSet
```Java
import java.util.HashSet;

HashSet<String> cars =  new Hashset<String> ();
cars.add();
cars.contains();
cars.remove();
cars.clear();
cars.size();
```

## HashMap
```Java
import java.util.HashMap;

HashMap<String,String> countryCapitals =  new HashMap<>();
countryCapitals.put("A","B");
countryCapitals.get("A");
countryCapitals.remove("A");
countryCapitals.clear();
countryCapitals.size();

for(String i : countryCapitals.keySet()){
	//keys
}

for (String i : countryCapitals.values()){
	//values
}
```