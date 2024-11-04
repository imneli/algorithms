function bubbleSort(arr) {
    let n = arr.length;
    let swapped;

    
    for (let i = 0; i < n; i++) {
        swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
    }

    return arr;
}

let array = [7, 2, 1, 6, 8, 5, 3, 4];
console.log("arr original:", array);
let sortedArray = bubbleSort(array);
console.log("arr ordenado:", sortedArray);
