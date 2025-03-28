/* eslint-disable */
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
    constructor(sqft, floors) {
        super(sqft);  // Appel du constructeur parent
        this._floors = floors;
    }

    // Getter pour floors
    get floors() {
        return this._floors;
    }

    // Redéfinition de la méthode evacuationWarningMessage
    evacuationWarningMessage() {
        return `Evacuate slowly the ${this._floors} floors`;
    }
}
