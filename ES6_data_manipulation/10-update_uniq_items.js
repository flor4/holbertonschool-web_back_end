function updateValue(value, KeyboardEvent, map) {
    if (value === 1) {
        map.set(KeyboardEvent, 100);
    }
}
export default function updateUniqItems(map) {
    if (!(map instanceof Map)) {
        throw new Error('Cannot process');
    }
    map.forEach(updateValue);
    return map;
}
