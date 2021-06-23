

def make_url(time):

    url_base = (
        "https://opendap.oceanobservatories.org/async_results/cstern@ldeo.columbia.edu/"
        "20210623T183800175Z-CP04OSSM-SBD11-06-METBKA000-telemetered-metbk_a_dcl_instrument"
        "/deployment0005_CP04OSSM-SBD11-06-METBKA000-telemetered-metbk_a_dcl_instrument_"
    )

    return f"{url_base}{time}.nc"


times = [
    '20160101T000102.577000-20160513T150947.552000',
    '20160527T155046.777000-20161012T150931.977000',
    '20161012T142641.906000-20161231T235909.571000',
]

