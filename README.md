# ucsb_evtlog

Main logic: [src/core/event_manager.py](https://github.com/MrRooots/ucsb_evtlog/blob/main/src/core/event_manager.py)
Configs: [src/config/config.py](https://github.com/MrRooots/ucsb_evtlog/blob/main/src/config/config.py)

Task solved using win32evtlog lib and win32evtlog.EvtQuery method for querying events data (see [query example](https://github.com/MrRooots/ucsb_evtlog/blob/main/expected_query.xml) and [query_manager](https://github.com/MrRooots/ucsb_evtlog/blob/main/src/core/query_manager.py))

To see available cmd params type: `python ./main.py --help`

Example: `python ./main.py COMPUTER_NAME --start_date=01.05.2029 --end_date=15.05.2029 --sid=USER_SID --make_excel`
