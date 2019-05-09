# ez-mode

Income tax calculation helpers for Canadians 🇨🇦 interning in the US 🇺🇸.

**Disclaimer**: I am not a tax professional, and none of the information from this project should be used directly. Consult with a tax professional and review all of the numbers before filing. I am not responsible for any incorrect results you submit :)

For the first iteration, I just want to get to a service that will consume W-2 data for typical internship income that a Canadian university student might receive in the US, and return line-by-line proposed values to enter into the 1040NR-EZ. Steps to get there:

- [x] JSON-file data source for tax brackets + code to map taxable income to tax.
- [ ] Logic to map W-2 data to the appropriate amount of taxable federal income.
- [ ] Wire together command-line input of W-2 boxes and proper output of 1040 lines.
- [ ] Some notion of "versioning" the data structures we'll use to represent the 1040NR-EZ document, to support it evolving over time from changes by the IRS.

Things I want to do after that:

- [ ] Reduce the number of assumptions about the filer (and also document these assumptions!)
- [ ] Front-end UI for all of the above.
- [ ] Support for state tax returns (e.g. California 540NR Short Form).
- [ ] Look for external APIs we can use as data sources rather than hard-coding line-number structures of documents and the tax brackets year-by-year.
