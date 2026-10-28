function swap(numbers){
    let reversed = [];
    for (let index = 0; index < numbers.length; index++) {
        reversed[index] = numbers[numbers.length - 1 - index];
    }
    return reversed;
}

function multipleArrays(numbers){
    let result = [];
    for (let index = 0; index < numbers.length; index++){
        result[index] = swap(numbers[index]);
    }
    return result;
}




let matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

let result = multipleArrays(matrix);

console.log(result);
