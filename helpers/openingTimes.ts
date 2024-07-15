// Helpers for calculating opening times of stations

import type { IOtJson } from '~/types/stations';

const moment = require('moment');
const momentTimezone = require('moment-timezone');

export function isStationOpen(date: Date, ot_json: IOtJson) {
  // Parse the input date
  const inputDate = moment(date);
  const inputDay = inputDate.day();
  const inputTime = inputDate.format('HH:mm');

  // Check for overrides
  if (ot_json.overrides) {
    for (let override of ot_json.overrides) {
      const startOverride = moment(override.startp);
      const endOverride = moment(override.endp);

      if (inputDate.isBetween(startOverride, endOverride, null, '[]')) {
        return !override.is_close;
      }
    }
  }

  // If there are no openingTimes, the station is always open
  if (!ot_json.openingTimes || ot_json.openingTimes.length === 0) {
    return true;
  }

  // Check the regular opening times
  for (let openingTime of ot_json.openingTimes) {
    const applicableDays = openingTime.applicable_days;

    // Check if the input day matches the applicable days
    if (applicableDays & (1 << inputDay)) {
      for (let period of openingTime.periods) {
        const startp = period.startp;
        const endp = period.endp;

        if (inputTime >= startp && inputTime <= endp) {
          return true;
        }
      }
    }
  }

  return false;
}

// Test example
// const ot_json = {
//     "openingTimes": [
//         {
//             "applicable_days": 31,
//             "periods": [
//                 {
//                     "startp": "05:00",
//                     "endp": "22:00"
//                 }
//             ]
//         },
//         {
//             "applicable_days": 96,
//             "periods": [
//                 {
//                     "startp": "07:00",
//                     "endp": "22:00"
//                 }
//             ]
//         }
//     ],
//     "overrides": [
//         {
//             "startp": "2017-06-05 05:00",
//             "endp": "2017-06-05 23:00",
//             "is_close": false
//         },
//         {
//             "startp": "2017-08-01 00:00",
//             "endp": "2017-09-01 00:00",
//             "is_close": true
//         }
//     ]
// };

// const testDate = "2017-06-05T10:00:00";
// console.log(isStationOpen(testDate, ot_json)); // Expected output: true
