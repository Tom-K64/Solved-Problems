"""
Problem Link:
https://leetcode.com/problems/design-browser-history/
"""

class BrowserHistory:
    def __init__(self, homepage):
        self._history, self._future = [], []
        self._current = homepage
    def visit(self, url):
        self._history.append(self._current)
        self._current = url
        self._future = []
    def back(self, steps):
        while steps > 0 and self._history:
            self._future.append(self._current)
            self._current = self._history.pop()
            steps -= 1
        return self._current
    def forward(self, steps):
        while steps > 0 and self._future:
            self._history.append(self._current)
            self._current = self._future.pop()
            steps -= 1
        return self._current
