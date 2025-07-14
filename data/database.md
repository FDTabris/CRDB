tables:

- Station
Id int, Region str, Name str, Location point, // NumPlatform int, NumTrack int
- Route
Id int, Region str, Name str, SpeedLimit float, //Length float, NumStation int, 
- Connection
FromRouteId int, ToRouteId int, FromDirection int, ToDirection int, StationId int, ReversalRequired bool, TrackCross int
- Segment
RouteId int, SegmentNo str, StationId int, LengthFromStart float, Electric bool, NumTrack //SpeedLimit float