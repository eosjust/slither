from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification


class PublicBurn(AbstractDetector):
    """
    Detect function named publicburn
    """

    ARGUMENT = "burn"  # slither will launch the detector with slither.py --mydetector
    HELP = "Function named publicburn (detector example)"
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = "https://github.com/trailofbits/slither/wiki/Adding-a-new-detector"
    WIKI_TITLE = "publicburn example"
    WIKI_DESCRIPTION = "Plugin example"
    WIKI_EXPLOIT_SCENARIO = ".."
    WIKI_RECOMMENDATION = ".."

    def _detect(self):
        results = []

        for contract in self.compilation_unit.contracts_derived:
            # Check if a function has 'publicburn' in its name
            for f in contract.functions:
                if "burn" in f.name:
                    # Info to be printed
                    info = ["burn function found in ", f, "\n"]

                    # Add the result in result
                    res = self.generate_result(info)

                    results.append(res)

        return results
