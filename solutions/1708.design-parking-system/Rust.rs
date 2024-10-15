/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */

 pub struct ParkingSystem {
    big: i32,
    medium: i32,
    small: i32,
}

impl ParkingSystem {
    // Constructor to initialize the parking system with the given number of slots for each type
    pub fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem { big, medium, small }
    }

    // Method to add a car of a specific type to the parking system
    pub fn add_car(&mut self, car_type: i32) -> bool {
        match car_type {
            1 => {
                if self.big > 0 {
                    self.big -= 1;
                    true
                } else {
                    false
                }
            }
            2 => {
                if self.medium > 0 {
                    self.medium -= 1;
                    true
                } else {
                    false
                }
            }
            3 => {
                if self.small > 0 {
                    self.small -= 1;
                    true
                } else {
                    false
                }
            }
            _ => false,
        }
    }
}
