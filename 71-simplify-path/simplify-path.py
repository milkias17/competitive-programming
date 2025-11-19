class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        splitted_path = filter(lambda x: x != "", path.split("/"))
        for segment in splitted_path:
            if segment == ".":
                continue
            if segment == "..":
                if len(path_stack) > 0:
                    path_stack.pop()
            else:
                path_stack.append(segment)
        
        return "/" + "/".join(path_stack)
