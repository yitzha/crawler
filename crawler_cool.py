import request
payload = {
'revAvailabilitySearch.SearchInfo.AdultCount':' 1',
'revAvailabilitySearch.SearchInfo.ChildrenCount':' 0',
'revAvailabilitySearch.SearchInfo.InfantCount':' 0',
'revAvailabilitySearch.SearchInfo.Direction':' Oneway',
'revAvailabilitySearch.SearchInfo.PromoCode':' ',
'revAvailabilitySearch.SearchInfo.SalesCode':' ',
'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode':' TPE',
'revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode':' NRT',
'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate':' 02/14/2020',
'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureStationCode':' ',
'revAvailabilitySearch.SearchInfo.SearchStations[1].ArrivalStationCode':' ',
'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureDate':' ',
'revAvailabilitySearch.DeepLink.OrganisationCode':' ',
'revAvailabilitySearch.DeepLink.Locale':' ',
'revAvailabilitySearch.SearchInfo.OrganisationToken':' ',
'revAvailabilitySearch.DeepLink.OrganisationToken':' ',
'revAvailabilitySearch.SearchInfo.MultiCurrencyCode':' TWD',
}
request.post('https://makeabooking.flyscoot.com/Book/?culture=zh-tw')