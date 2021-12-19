"""Restaurant rating lister."""


# put your code here
rating = {"Florean Fortescue's Ice Cream Parlour":4,
          "Jellied Eel Shop":3,
          "The Tavern":3,
          "Luchino Caffe":1,
          "The Porcupine":5,
          "Diagon Alley cafe":2,
          "The Bear & Staff":2,
          "Ministry Munchies":1,
          "Chip Shop":3,
          "Eternelle's Elixir of Refreshment":5,
          "Big Bean Shack":3,
          "The Club":2
}
k=input("Restaurant name?:")
v=input("Restaurant rating?:")



a = sorted(rating.items(), key=lambda x: x[1])
print(a)