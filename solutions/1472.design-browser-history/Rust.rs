struct BrowserHistory {
    back_stack: Vec<String>,
    forward_stack: Vec<String>,
    current: String,
}

impl BrowserHistory {
    fn new(homepage: String) -> Self {
        BrowserHistory {
            back_stack: Vec::new(),
            forward_stack: Vec::new(),
            current: homepage,
        }
    }

    fn visit(&mut self, url: String) {
        self.back_stack.push(self.current.clone());
        self.current = url;
        self.forward_stack.clear();
    }

    fn back(&mut self, steps: i32) -> String {
        for _ in 0..steps {
            if self.back_stack.is_empty() {
                break;
            }
            self.forward_stack.push(self.current.clone());
            self.current = self.back_stack.pop().unwrap();
        }
        self.current.clone()
    }

    fn forward(&mut self, steps: i32) -> String {
        for _ in 0..steps {
            if self.forward_stack.is_empty() {
                break;
            }
            self.back_stack.push(self.current.clone());
            self.current = self.forward_stack.pop().unwrap();
        }
        self.current.clone()
    }
}