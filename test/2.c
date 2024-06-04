#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_ROOMS 10
#define MAX_NAME_LENGTH 50
#define MAX_DESC_LENGTH 200
#define MAX_INVENTORY_SIZE 10

typedef struct {
  char name[MAX_NAME_LENGTH];
  char description[MAX_DESC_LENGTH];
  int north;
  int south;
  int east;
  int west;
  int items[MAX_INVENTORY_SIZE];
  int num_items;
} Room;

typedef struct {
  char name[MAX_NAME_LENGTH];
} Item;

Room rooms[MAX_ROOMS];
Item inventory[MAX_INVENTORY_SIZE];
int current_room;
int num_items_in_inventory;

void initialize_game() {
  // Seed random number generator
  srand(time(NULL));

  // Set up rooms
  strcpy(rooms[0].name, "Forest Clearing");
  strcpy(rooms[0].description, "You find yourself in a sun-dappled forest clearing. Birds chirp in the trees, and a gentle breeze rustles the leaves.");
  rooms[0].north = 1;
  rooms[0].south = -1;
  rooms[0].east = -1;
  rooms[0].west = -1;
  rooms[0].num_items = 0;

  strcpy(rooms[1].name, "Cave Entrance");
  strcpy(rooms[1].description, "A dark cave entrance looms before you. A cold wind emanates from within.");
  rooms[1].north = -1;
  rooms[1].south = 0;
  rooms[1].east = -1;
  rooms[1].west = -1;
  rooms[1].items[0] = 2;
  rooms[1].num_items = 1;

  // ... (set up remaining rooms and items)

  current_room = 0;
  num_items_in_inventory = 0;
}

void print_room_description() {
  printf("%s\n\n", rooms[current_room].description);
}

void list_exits() {
  printf("Exits:\n");
  if (rooms[current_room].north != -1) {
    printf("North\n");
  }
  if (rooms[current_room].south != -1) {
    printf("South\n");
  }
  if (rooms[current_room].east != -1) {
    printf("East\n");
  }
  if (rooms[current_room].west != -1) {
    printf("West\n");
  }
}

void list_inventory() {
  if (num_items_in_inventory == 0) {
    printf("You have no items in your inventory.\n");
    return;
  }
  printf("Inventory:\n");
  for (int i = 0; i < num_items_in_inventory; i++) {
    printf("- %s\n", inventory[i].name);
  }
}

int get_item_index(const char* name) {
  for (int i = 0; i < num_items_in_inventory; i++) {
    if (strcmp(inventory[i].name, name) == 0) {
      return i;
    }
  }
  return -1;
}

void take_item(const char* name) {
  int item_index = get_item_index(name);
  if (item_index == -1) {
    printf("You don't have that item.\n");
    return;
  }
  if (num_items_in_inventory == MAX_INVENTORY_SIZE) {
    printf("Your inventory is full.\n");
    return;
  }

  // Move item from room to inventory
  strcpy(inventory[num_items_in_inventory].name, name);
  num_items_in_inventory++;
  rooms[current_room].items[item_index] = -1; // Mark item as taken
}

void drop_item(const char* name) {
  int item_index = get_item_index(
