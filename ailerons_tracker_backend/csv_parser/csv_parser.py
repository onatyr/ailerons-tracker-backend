""" CSV file parser middleware """
from operator import itemgetter
import sys
from ailerons_tracker_backend.errors import ParserError
from ailerons_tracker_backend.models.record_model import Record
from ailerons_tracker_backend.models.record_field_model import LocalisationField, DepthField
from ailerons_tracker_backend.utils.file_util import FileManager, FileFieldName, File


class CsvParser:
    """Class that manage the parsing of the different csv"""

    def __init__(self, loc_file, depth_file):
        self.loc_df = self._parse_field_from_csv(
            loc_file)
        self.depth_df = self._parse_field_from_csv(depth_file)
        self.record_list = self._merge_lists

    def _parse_field_from_csv(self, file: File):
        try:
            file_df = FileManager().get_dataframe(file.path)
            data_list = []

            field_class = LocalisationField if file.field_name == FileFieldName.LOCALISATION else DepthField

            for row in file_df.itertuples(index=False):
                new_field_record = field_class(row._asdict(), file.db_id)
                new_field_record.file_db_id = file.db_id
                data_list.append(new_field_record.__dict__)

            return data_list

        except Exception as e:
            raise ParserError() from e

    def _merge_lists(self):
        loc_list = sorted(self.loc_df, key=itemgetter('record_timestamp'))
        depth_list = sorted(self.depth_df, key=itemgetter('record_timestamp'))

        merged_list = []

        i = 0
        j = 0
        while i <= len(loc_list) and j <= len(depth_list):
            if loc_list[i].record_timestamp == depth_list[j].record_timestamp:
                merged_list.append(
                    Record(localisation_field_record=loc_list[i], depth_field_record=depth_list[j]).to_dict())
                i += 1
                j += 1
            else:
                if depth_list[j] < loc_list[i]:
                    j += 1
                else:
                    i += 1

        return merged_list
