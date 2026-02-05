class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_filepath = defaultdict(list)
        for path in paths:
            split_path = path.split(" ")
            base_path = split_path[0]
            for _file in split_path[1:]:
                file_name = []
                content = []
                i = 0
                while _file[i] != "(":
                    file_name.append(_file[i])
                    i += 1
                i += 1
                while _file[i] != ")":
                    content.append(_file[i])
                    i += 1

                content_filepath["".join(content)].append(f"{base_path}/{''.join(file_name)}")
        
        res = []
        for k, v in content_filepath.items():
            if len(v) > 1:
                res.append(v)
        return res