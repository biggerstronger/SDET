schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "value": {
          "type": "string"
        },
        "_id": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "value",
        "_id"
      ]
    },
    "statistic": {
      "type": "object",
      "properties": {
        "workhoursPercents": {
          "type": "integer"
        },
        "maxHours": {
          "type": "integer"
        },
        "minHours": {
          "type": "integer"
        },
        "E95": {
          "type": "integer"
        },
        "E68": {
          "type": "integer"
        },
        "E50": {
          "type": "integer"
        },
        "reduced": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "workhoursPercents",
        "maxHours",
        "minHours",
        "E95",
        "E68",
        "E50",
        "reduced"
      ]
    },
    "_id": {
      "type": "string"
    },
    "riskHistory": {
      "type": "array",
      "items": {}
    },
    "statusHistory": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "status": {
              "type": "object",
              "properties": {
                "_id": {
                  "type": "string"
                },
                "value": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "required": [
                "_id",
                "value",
                "name"
              ]
            },
            "_id": {
              "type": "string"
            },
            "user": {
              "type": "object",
              "properties": {
                "_id": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "role": {
                  "type": "string"
                }
              },
              "required": [
                "_id",
                "name",
                "role"
              ]
            },
            "created": {
              "type": "string"
            }
          },
          "required": [
            "status",
            "_id",
            "user",
            "created"
          ]
        }
      ]
    },
    "created": {
      "type": "string"
    },
    "linkToCRM": {
      "type": "null"
    },
    "phases": {
      "type": "array",
      "items": {}
    },
    "risk": {
      "type": "integer"
    },
    "useOfStandart": {
      "type": "integer"
    },
    "files": {
      "type": "array",
      "items": {}
    },
    "departments": {
      "type": "array",
      "items": {}
    },
    "approvers": {
      "type": "array",
      "items": {}
    },
    "managers": {
      "type": "array",
      "items": {}
    },
    "locale": {
      "type": "string"
    },
    "authors": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "isLocked": {
      "type": "boolean"
    },
    "description": {
      "type": "null"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "status",
    "statistic",
    "_id",
    "riskHistory",
    "statusHistory",
    "created",
    "linkToCRM",
    "phases",
    "risk",
    "useOfStandart",
    "files",
    "departments",
    "approvers",
    "managers",
    "locale",
    "authors",
    "isLocked",
    "description",
    "name"
  ]
}