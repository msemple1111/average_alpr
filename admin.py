#!bin/python
import json
print("Welcome to the interrative terminal")
#you = input("average_speed_admin_utillity> ")
data = json.loads("""
{
  "uuid": "e11e0acc-6aaf-4817-9299-9e6773043b8e",
  "camera_id": 1,
  "site_id": "watchtower-hq",
  "img_width": 640,
  "img_height": 480,
  "epoch_time": 1402161050,
  "processing_time_ms": 138.669163,
  "results": [
    {
      "plate": "S11FRE",
      "confidence": 77.130661,
      "matches_template": 0,
      "region": "",
      "region_confidence": 0,
      "coordinates": [
        {
          "x": 218,
          "y": 342
        },
        {
          "x": 407,
          "y": 325
        },
        {
          "x": 407,
          "y": 413
        },
        {
          "x": 218,
          "y": 431
        }
      ],
      "candidates": [
        {
          "plate": "S11FRE",
          "confidence": 77.130661,
          "matches_template": 0
        },
        {
          "plate": "S11ERE",
          "confidence": 75.496307,
          "matches_template": 0
        },
        {
          "plate": "S11RE",
          "confidence": 75.440361,
          "matches_template": 0
        },
        {
          "plate": "S11CRE",
          "confidence": 75.340179,
          "matches_template": 0
        },
        {
          "plate": "S11FHE",
          "confidence": 75.240974,
          "matches_template": 0
        },
        {
          "plate": "S11EHE",
          "confidence": 73.606621,
          "matches_template": 0
        },
        {
          "plate": "S11HE",
          "confidence": 73.550682,
          "matches_template": 0
        },
        {
          "plate": "S11CHE",
          "confidence": 73.450493,
          "matches_template": 0
        },
        {
          "plate": "S11FBE",
          "confidence": 71.782944,
          "matches_template": 0
        },
        {
          "plate": "S11FE",
          "confidence": 71.762756,
          "matches_template": 0
        },
        {
          "plate": "S11EBE",
          "confidence": 70.148582,
          "matches_template": 0
        },
        {
          "plate": "S11EE",
          "confidence": 70.128403,
          "matches_template": 0
        },
        {
          "plate": "S11BE",
          "confidence": 70.092636,
          "matches_template": 0
        },
        {
          "plate": "S11E",
          "confidence": 70.072449,
          "matches_template": 0
        },
        {
          "plate": "S11CBE",
          "confidence": 69.992455,
          "matches_template": 0
        },
        {
          "plate": "S11CE",
          "confidence": 69.972267,
          "matches_template": 0
        },
        {
          "plate": "S11FME",
          "confidence": 69.581451,
          "matches_template": 0
        },
        {
          "plate": "S11F8E",
          "confidence": 68.718605,
          "matches_template": 0
        },
        {
          "plate": "S11EME",
          "confidence": 67.947098,
          "matches_template": 0
        },
        {
          "plate": "S11ME",
          "confidence": 67.891144,
          "matches_template": 0
        },
        {
          "plate": "S11CME",
          "confidence": 67.790962,
          "matches_template": 0
        },
        {
          "plate": "S11F9E",
          "confidence": 67.744087,
          "matches_template": 0
        },
        {
          "plate": "S11E8E",
          "confidence": 67.084251,
          "matches_template": 0
        },
        {
          "plate": "S118E",
          "confidence": 67.028305,
          "matches_template": 0
        },
        {
          "plate": "S11C8E",
          "confidence": 66.928123,
          "matches_template": 0
        }
      ]
    },
    {
      "plate": "EJLESSIE",
      "epoch_time": 1402158050,
      "confidence": 78.167984,
      "matches_template": 0,
      "region": "",
      "region_confidence": 0,
      "processing_time_ms": 51.650604,
      "coordinates": [
        {
          "x": 226,
          "y": 369
        },
        {
          "x": 348,
          "y": 348
        },
        {
          "x": 355,
          "y": 406
        },
        {
          "x": 231,
          "y": 429
        }
      ],
      "candidates": [
        {
          "plate": "EJLESSIE",
          "confidence": 78.167984,
          "matches_template": 0
        },
        {
          "plate": "VI5A",
          "confidence": 58.167984,
          "matches_template": 0
        },
        {
          "plate": "EDLESSIE",
          "confidence": 77.61319,
          "matches_template": 0
        }
      ]
    }
  ]
}
""")


print(data['results'][0]['plate'])