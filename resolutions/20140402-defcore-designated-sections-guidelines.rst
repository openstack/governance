===================================================
 2014-04-02 DefCore Designated Sections Guidelines
===================================================

This resolution is about formally approving the general selection principles
for "designated sections" of code, as part of the DefCore effort.

Sections of code should generally be DESIGNATED when:

- code provides the project external REST API, or
- code is shared and provides common functionality for all options, or
- code implements logic that is critical for cross-platform operation

Sections of code should generally NOT be DESIGNATED when:

- code interfaces to vendor-specific functions, or
- project design explicitly intended this section to be replaceable, or
- code extends the project external REST API in a new or different way, or
- code is being deprecated

Code that is not clearly designated is assumed to be designated unless
determined otherwise. The default assumption will be to consider code
designated.
