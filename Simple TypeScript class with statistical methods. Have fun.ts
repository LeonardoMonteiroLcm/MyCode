export class StatLab {
    constructor() { }

    //==================================================
    // Utilities
    //==================================================

    public isEven(n: number): boolean {
        return n % 2 === 0;
    }

    public isOdd(n: number): boolean {
        return n % 2 !== 0;
    }

    public sumNumbers(sample: number[]): number {
        return sample.reduce((total, n) => total + n, 0);
    }

    //==================================================
    // Graphs
    //==================================================

    public histogram(sample: number[]): [number[], number[]] {
        let xlist: number[] = [];
        let ylist: number[] = [];

        if (sample.length > 0) {
            let sortedSample = [...sample].sort((a, b) => a - b);
            xlist.push(sortedSample[0]);
            ylist.push(0);
            let i = 0;

            for (let x of sortedSample) {
                if (x <= xlist[i]) {
                    ylist[i] += 1;
                } else {
                    xlist.push(x);
                    ylist.push(1);
                    i += 1;
                }
            }
        }
        return [xlist, ylist];
    }

    public ogive(sample: number[]): [number[], number[]] {
        let [xlist, ylist] = this.histogram(sample);
        for (let i = 1; i < ylist.length; i++) {
            ylist[i] += ylist[i - 1];
        }
        return [xlist, ylist];
    }

    public pareto(sample: number[]): [number[], number[]] {
        let pxlist: number[] = [];
        let pylist: number[] = [];

        if (sample.length > 0) {
            let [xlist, ylist] = this.histogram(sample);
            pxlist.push(xlist[0]);
            pylist.push(ylist[0]);

            for (let i = 1; i < ylist.length; i++) {
                let inserted = false;
                for (let j = 0; j < pylist.length; j++) {
                    if (ylist[i] >= pylist[j]) {
                        pxlist.splice(j, 0, xlist[i]);
                        pylist.splice(j, 0, ylist[i]);
                        inserted = true;
                        break;
                    }
                }
                if (!inserted) {
                    pxlist.push(xlist[i]);
                    pylist.push(ylist[i]);
                }
            }
        }
        return [pxlist, pylist];
    }

    public pmf(sample: number[]): [number[], number[]] {
        let [xlist, ylist] = this.histogram(sample);
        let n = sample.length;
        ylist = ylist.map(y => y / n);
        return [xlist, ylist];
    }

    public cmf(sample: number[]): [number[], number[]] {
        let [xlist, ylist] = this.ogive(sample);
        let n = sample.length;
        ylist = ylist.map(y => y / n);
        return [xlist, ylist];
    }

    //==================================================
    // Measures of Central Tendency
    //==================================================

    public weightedMean(weights: number[], sample: number[]): number {
        if (sample.length === 0 || sample.length !== weights.length) {
            return NaN;
        }
        let sum = 0;
        for (let i = 0; i < sample.length; i++) {
            sum += weights[i] * sample[i];
        }
        return sum / weights.reduce((a, b) => a + b, 0);
    }

    public mean(sample: number[]): number {
        if (sample.length === 0) return NaN;
        return sample.reduce((sum, val) => sum + val, 0) / sample.length;
    }

    public median(sample: number[]): number {
        if (sample.length === 0) return NaN;
        let sortedSample = [...sample].sort((a, b) => a - b);
        let mid = Math.floor(sortedSample.length / 2);

        return this.isOdd(sortedSample.length)
            ? sortedSample[mid]
            : (sortedSample[mid - 1] + sortedSample[mid]) / 2;
    }

    public mode(sample: number[]): number {
        if (sample.length === 0) return NaN;
        let [xlist, ylist] = this.histogram(sample);
        let maxFrequency = Math.max(...ylist);
        return xlist[ylist.indexOf(maxFrequency)];
    }

    public range(sample: number[]): [number, number] {
        if (sample.length === 0) return [NaN, NaN];
        let sortedSample = [...sample].sort((a, b) => a - b);
        return [sortedSample[0], sortedSample[sortedSample.length - 1]];
    }

    public amplitude(sample: number[]): number {
        let [min, max] = this.range(sample);
        return max - min;
    }

    public midrange(sample: number[]): number {
        if (sample.length === 0) return NaN;
        let sortedSample = [...sample].sort((a, b) => a - b);
        return (sortedSample[0] + sortedSample[sortedSample.length - 1]) / 2;
    }

    public midpoint: Function = this.midrange;

    //==================================================
    // Measures of Variation
    //==================================================

    public sumSquares(sample: number[]): number {
        if (sample.length === 0) return NaN;
        let mean = sample.reduce((a, b) => a + b, 0) / sample.length;
        return sample.reduce((sum, x) => sum + (x - mean) ** 2, 0);
    }

    public variancePop(pop: number[]): number {
        if (pop.length === 0) return NaN;
        return this.sumSquares(pop) / pop.length;
    }

    public varianceSample(sample: number[]): number {
        if (sample.length <= 1) return NaN;
        return this.sumSquares(sample) / (sample.length - 1);
    }

    public variance: Function = this.varianceSample;

    public stdDevPop(pop: number[]): number {
        return Math.sqrt(this.variancePop(pop));
    }

    public stdDevSample(sample: number[]): number {
        return Math.sqrt(this.varianceSample(sample));
    }

    public stdDev: Function = this.stdDevSample;

    public chebyshev(k: number): number {
        if (k <= 1) throw new Error("k must be > 1");
        return 1 - 1 / (k * k);
    }

    //==================================================
    // Measures of Position
    //==================================================

    public zscoresPop(sample: number[]): number {
        //...Sorry, I'm too lazy to code this right now. By the way, code yourselves!
        return 0;
    }

    public zscoresSample(sample: number[]): number {
        //...Sorry, I'm too lazy to code this right now. By the way, code yourselves!
        return 0;
    }

    public zscores: Function = this.zscoresSample;

    public percentileRank(x: number, sample: number[]): number {
        //...Sorry, I'm too lazy to code this right now. By the way, code yourselves!
        return 0;
    }

    public percentile(rank: number, sample: number[]): number {
        if (sample.length === 0 || rank <= 0 || rank > 100) return NaN;
        let sortedSample = [...sample].sort((a, b) => a - b);
        let i = (sortedSample.length - 1) * (rank / 100);
        let f = Math.floor(i);
        let c = Math.ceil(i);
        return f === c ? sortedSample[i] : sortedSample[f] * (c - i) + sortedSample[c] * (i - f);
    }

    public percentile2(rank: number, sample: number[]): number {
        if (sample.length === 0 || rank < 0 || rank > 100) return NaN;
        let sortedSample = [...sample].sort((a, b) => a - b);
        let i = (sortedSample.length - 1) * (rank / 100);
        let f = Math.floor(i);
        let c = Math.ceil(i);
        if (f === c) { return sortedSample[f]; }
        return sortedSample[f] + (i - f) * (sortedSample[c] - sortedSample[f]);
    }

    public decile(rank: number, sample: number[]): number {
        return this.percentile(10 * rank, sample);
    }

    public quartile(rank: number, sample: number[]): number {
        return this.percentile(25 * rank, sample);
    }
}
