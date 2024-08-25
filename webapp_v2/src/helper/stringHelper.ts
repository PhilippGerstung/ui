/**
 * Splits an arbitrary string into an arrray of strings separated by a space character and capitalizes the first letter of each word.
 * The rest of each string is converted to lowercase.
 * @param str 
 */
export function capitalizeFirstLetter(str: string): string {
    return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join(' ');
}