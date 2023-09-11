export function pythonCaseToCapitalizedWords(s) {
    return s
        .split("_")
        .map((word) => word[0].toUpperCase() + word.slice(1))
        .join(" ");
}

export function camelCaseToCapitalizedWords(s) {
    return s
        .split(/(?=[A-Z])/)
        .map((word) => word[0].toUpperCase() + word.slice(1))
        .join(" ");
}