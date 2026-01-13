export default function getStudentsIdsSum(array) {
    return array.reduce((accumulator, object) => accumulator + object.id, 0);
}
