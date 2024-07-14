// @vitest-environment node
import { expect, test } from 'vitest'
import {isStationOpen} from '../helpers/openingTimes'


const ot_json = {
      "openingTimes": [
          {
              "applicable_days": 31,
              "periods": [
                  {
                      "startp": "05:00",
                      "endp": "22:00"
                  }
              ]
          },
          {
              "applicable_days": 96,
              "periods": [
                  {
                      "startp": "07:00",
                      "endp": "22:00"
                  }
              ]
          }
      ],
      "overrides": [
          {
              "startp": "2017-06-05 05:00",
              "endp": "2017-06-05 23:00",
              "is_close": false
          },
          {
              "startp": "2017-08-01 00:00",
              "endp": "2017-09-01 00:00",
              "is_close": true
          }
      ]
  };


test("always open", () => {
  expect(isStationOpen(new Date("2017-06-05T10:00:00"), {})).toBe(true)
});

test('open at "2017-06-05T10:00:00"', () => {
  const result = isStationOpen(new Date("2017-06-05T10:00:00"), ot_json);
  expect(result).toBe(true)
})

test('closed at "2017-06-05T02:00:00"', () => {
  const result = isStationOpen(new Date("2017-06-05T02:00:00"), ot_json);
  expect(result).toBe(false)
})