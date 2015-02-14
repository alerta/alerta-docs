

enum Severity {
  CRITICAL = 1,
  MAJOR = 2,
  MINOR = 3,
  WARNING = 4,
  INDETER = 5,
  CLEARED =5,
  NORMAL = 5,
  OK = 5,
  INFORM = 6,
  DEBUG = 7,
  AUTH = 8,
  UNKNOWN = 9,
}

enum TrendIndication {
  MORE_SEVERE = 1,
  LESS_SEVERE = 2,
  NO_CHANGE = 3,
}

enum Status {
  OPEN = 1,
  ASSIGN = 2,
  ACK = 3,
  CLOSED = 4,
  EXPIRED = 5,
  UNKNOWN = 9,
}

enum EventType {
  ALERT = 0,
  SNMP_TRAP = 1,
  SNMP_NOTIF = 2,
  IPMI_PET = 3,
  SYSLOG = 4,
  CHECK = 5,
  PROBE = 6,
  ENVIRON = 7,
  OTHER = 8,
  HEARTBEAT = 9
}

typedef string UUIDType  /* UUID(4) */
typedef string Timestamp /* ISO-8601 */

struct History {
  1: UUIDType id,
  2: required string event,
  3: optional Severity severity,
  4: optional Status status,
  5: optional string value,
  6: optional string text,
  7: optional Timestamp updateTime,
}

struct Alert {
  1: UUIDType id,
  2: required string resource,
  3: required string event,
  4: optional string environment,
  5: optional Severity severity = Severity.NORMAL,
  6: optional list<string> correlate,
  7: optional Status status,
  8: optional list<string> service_,
  9: optional string group,
  10: optional string value,
  11: optional string text,
  12: optional list<string> tags,
  13: optional map<string,string> attributes,
  14: optional string origin,
  15: optional EventType type = EventType.ALERT,
  16: optional Timestamp createTime,
  17: optional i32 timeout = 0,
  18: optional string rawData,
  19: optional i64 duplicateCount,
  20: optional bool repeat,
  21: optional Severity previousSeverity,
  22: optional TrendIndication trendIndication,
  23: optional Timestamp receiveTime,
  24: optional UUIDType lastReceiveId,
  25: optional Timestamp lastReceiveTime,
  26: optional History history
}

struct Heartbeat {
  1: UUIDType id,
  2: required string origin,
  3: optional list<string> tags,
  4: required EventType type = EventType.HEARTBEAT,
  5: optional Timestamp createTime,
  6: optional i32 timeout = 0,
  7: optional Timestamp receiveTime
}
