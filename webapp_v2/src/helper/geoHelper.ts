
/**
 * Calculate the distance between two points on the Earth's surface using the Haversine formula. Returns the distance in Km.
 * @param lat1 
 * @param lon1 
 * @param lat2 
 * @param lon2 
 * @returns 
 */
export function kmDistanceBetweenCoordinates(lat1: number, lon1: number, lat2: number, lon2: number): number {
    function toRadians(degrees: number) {
        return degrees * (Math.PI / 180);
    }

    const R = 6371; // Radius of the Earth in kilometers
    const dLat = toRadians(lat2 - lat1);
    const dLon = toRadians(lon2 - lon1);
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(toRadians(lat1)) * Math.cos(toRadians(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c; // Distance in kilometers

    return distance;
}