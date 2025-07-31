import { expect } from "chai";
import kue from 'kue';
import createPushNotificationsJobs from "./8-job.js";

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('display a error message if jobs is not an array', () => {
        expect(() => {
            createPushNotificationsJobs('not an array', queue);
        }).to.throw('Jobs is not an array');
    });

    it('create two new jobs to the queue', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            }
        ];
        
        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal({
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        });
        expect(queue.testMode.jobs[1].data).to.deep.equal({
            phoneNumber: '4153518781',
            message: 'This is the code 4562 to verify your account'
        });
    });

    it('create no jobs for an empty array', () => {
        const jobs = [];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(0);
    });

    it('create one job for array with one element', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(1);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    });
});