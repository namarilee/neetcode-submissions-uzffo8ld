class MinStack {
    private var stack: [Int] = []
    private var minStack: [Int] = []
    
    init() {}

    func push(_ val: Int) {
        stack.append(val)
        let currentMin = minStack.last ?? val
        minStack.append(min(val, currentMin))
    }

    func pop() {
        stack.removeLast()
        minStack.removeLast()
    }

    func top() -> Int {
        return stack.last ?? 0
    }

    func getMin() -> Int {
        return minStack.last ?? 0
    }
}