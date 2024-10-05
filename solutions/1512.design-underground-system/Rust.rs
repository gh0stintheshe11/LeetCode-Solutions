use std::collections::HashMap;

struct UndergroundSystem {
    check_in_data: HashMap<i32, (String, i32)>,
    travel_data: HashMap<(String, String), (i32, i32)>,
}

impl UndergroundSystem {
    fn new() -> Self {
        UndergroundSystem {
            check_in_data: HashMap::new(),
            travel_data: HashMap::new(),
        }
    }

    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.check_in_data.insert(id, (station_name, t));
    }

    fn check_out(&mut self, id: i32, station_name: String, t: i32) {
        if let Some((start_station, start_time)) = self.check_in_data.remove(&id) {
            let travel_time = t - start_time;
            let entry = self.travel_data.entry((start_station.clone(), station_name.clone()))
                .or_insert((0, 0));
            entry.0 += travel_time;
            entry.1 += 1;
        }
    }

    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        if let Some(&(total_time, trip_count)) = self.travel_data.get(&(start_station, end_station)) {
            return total_time as f64 / trip_count as f64;
        }
        0.0
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */
