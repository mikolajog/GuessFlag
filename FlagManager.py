from constants import FLAG_PAGE_CAPACITY
import math

class FlagPagingManager(object):
    def get_current_flags_page(self, flag_list, page):
        start_flag_idx = page * FLAG_PAGE_CAPACITY
        n_flags = min(FLAG_PAGE_CAPACITY, len(flag_list))

        return flag_list[start_flag_idx:(start_flag_idx + n_flags)]

    def get_possible_page_count(self, flag_list):
        return math.ceil((len(flag_list)*1.0/FLAG_PAGE_CAPACITY))