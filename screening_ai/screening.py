from typing import Any, List, Dict, Optional, Union
from pydantic import BaseModel

from screening_ai.api.platform_screening_jobs_api import PlatformScreeningJobsApi
from screening_ai.api.platform_screening_submissions_api import PlatformScreeningSubmissionsApi
from screening_ai.api.platform_screening_templates_api import PlatformScreeningTemplatesApi
from screening_ai.api_client import ApiClient
from screening_ai.models import (
    PlatformCreateScreeningJobDto,
    CreateScreeningTemplateDto,
    GenerateScreeningTemplateQuestionsDto,
    CreatePlatformScreeningFormSubmissionDto,
    UpdatePlatformScreeningSubmissionChatDto,
    GetPlatformScreeningSubmissionsOfOrgDto,
    UpdatePlatformScreeningSubmissionsStatusDto,
    CreatePlatformScreeningSubmissionStreamingRoomTokenDto,
)


class ScreeningAI:
    def __init__(self, org_api_key: str, base_url: str = "http://localhost:3000"):
        """
        Initialize the Screening AI client.

        :param org_api_key: The organization's API key.
        :param base_url: The base URL of the API (defaults to production).
        """
        self.api_client = ApiClient(header_name="X-API-KEY", header_value=org_api_key)
        self.api_client.configuration.host = base_url

        # Initialize API clients
        self.screening_jobs_api = PlatformScreeningJobsApi(self.api_client)
        self.screening_templates_api = PlatformScreeningTemplatesApi(self.api_client)
        self.screening_submissions_api = PlatformScreeningSubmissionsApi(self.api_client)

    # --- Screening Jobs ---
    def create_screening_job(
        self,
        screening_template_id: str,
        title: str,
        job_active: bool,
        jd: str,
        upvotes: List[str],
        created_at: str,
    ) -> Dict[str, Any]:
        """
        Create a new screening job.

        :param screening_template_id: The ID of the screening template.
        :param title: The title of the screening job.
        :param job_active: Whether the job is active.
        :param jd: The job description.
        :param upvotes: A list of upvotes.
        :param created_at: The creation timestamp.
        :return: API response.
        """
        job_data = PlatformCreateScreeningJobDto(
            screening_template_id=screening_template_id,
            title=title,
            job_active=job_active,
            jd=jd,
            upvotes=upvotes,
            created_at=created_at,
        )
        return self.screening_jobs_api.platform_screening_jobs_controller_create_screening_job(
            platform_create_screening_job_dto=job_data
        )

    def get_screening_jobs_of_org(self) -> Dict[str, Any]:
        """
        Get all screening jobs of the organization.

        :return: API response.
        """
        return self.screening_jobs_api.platform_screening_jobs_controller_get_screening_jobs_of_org()

    def get_screening_job_by_id(self, screening_job_id: str) -> Dict[str, Any]:
        """
        Get a screening job by its ID.

        :param screening_job_id: The ID of the screening job.
        :return: API response.
        """
        return self.screening_jobs_api.platform_screening_jobs_controller_get_screening_job_using_id(
            screening_job_id=screening_job_id
        )

    # --- Screening Templates ---
    def create_screening_template(
        self,
        title: str,
        description: str,
        prompt: str,
        is_streaming: bool,
        questions: List[str],
        created_at: str,
    ) -> Dict[str, Any]:
        """
        Create a new screening template.

        :param title: The title of the template.
        :param description: The description of the template.
        :param prompt: The prompt for the template.
        :param is_streaming: Whether the template supports streaming.
        :param questions: A list of questions.
        :param created_at: The creation timestamp.
        :return: API response.
        """
        template_data = CreateScreeningTemplateDto(
            title=title,
            description=description,
            prompt=prompt,
            is_streaming=is_streaming,
            questions=questions,
            created_at=created_at,
        )
        return self.screening_templates_api.platform_screening_templates_controller_create_screening_template(
            create_screening_template_dto=template_data
        )

    def get_screening_templates(self) -> Dict[str, Any]:
        """
        Get all screening templates of the organization.

        :return: API response.
        """
        return self.screening_templates_api.platform_screening_templates_controller_get_screening_templates()

    def generate_screening_template_questions(self, job_title: str) -> Dict[str, Any]:
        """
        Generate screening template questions.

        :param job_title: The title of the job.
        :return: API response.
        """
        questions_data = GenerateScreeningTemplateQuestionsDto(job_title=job_title)
        return self.screening_templates_api.platform_screening_templates_controller_generate_screening_template_questions(
            generate_screening_template_questions_dto=questions_data
        )

    # --- Screening Submissions ---
    def create_screening_submission(
        self,
        org_id: str,
        org_alias: str,
        email: str,
        first_name: str,
        last_name: str,
        phone_number: str,
        screening_job_id: str,
        chat: List[str],
        created_at: str,
        status: str,
        upvotes: List[str],
        is_viewed: bool,
        is_private: bool,
    ) -> Dict[str, Any]:
        """
        Create a new screening submission.

        :param org_id: The organization ID.
        :param org_alias: The organization alias.
        :param email: The email of the candidate.
        :param first_name: The first name of the candidate.
        :param last_name: The last name of the candidate.
        :param phone_number: The phone number of the candidate.
        :param screening_job_id: The ID of the screening job.
        :param chat: A list of chat messages.
        :param created_at: The creation timestamp.
        :param status: The status of the submission.
        :param upvotes: A list of upvotes.
        :param is_viewed: Whether the submission has been viewed.
        :param is_private: Whether the submission is private.
        :return: API response.
        """
        submission_data = CreatePlatformScreeningFormSubmissionDto(
            org_id=org_id,
            org_alias=org_alias,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            screening_job_id=screening_job_id,
            chat=chat,
            created_at=created_at,
            status=status,
            upvotes=upvotes,
            is_viewed=is_viewed,
            is_private=is_private,
        )
        return self.screening_submissions_api.platform_screening_submissions_controller_create_screening_submission(
            create_platform_screening_form_submission_dto=submission_data
        )

    def update_screening_submission_chat(
        self,
        screening_submission_id: str,
        index: int,
        human: str,
        human_audio_url: str,
        answer_type: str,
    ) -> Dict[str, Any]:
        """
        Update screening submission chat.

        :param screening_submission_id: The ID of the screening submission.
        :param index: The index of the question.
        :param human: The human answer.
        :param human_audio_url: The URL of the human audio answer.
        :param answer_type: The type of answer.
        :return: API response.
        """
        chat_data = UpdatePlatformScreeningSubmissionChatDto(
            screening_submission_id=screening_submission_id,
            index=index,
            human=human,
            human_audio_url=human_audio_url,
            answer_type=answer_type,
        )
        return self.screening_submissions_api.platform_screening_submissions_controller_update_screening_submission_chat(
            update_platform_screening_submission_chat_dto=chat_data
        )

    def get_screening_submissions_by_job_id(self, job_id: str) -> Dict[str, Any]:
        """
        Get screening submissions by job ID.

        :param job_id: The ID of the job.
        :return: API response.
        """
        return self.screening_submissions_api.platform_screening_submissions_controller_get_screening_submissions_using_job_id(
            job_id=job_id
        )

    def get_screening_submission_by_id(self, screening_submission_id: str) -> Dict[str, Any]:
        """
        Get a screening submission by its ID.

        :param screening_submission_id: The ID of the screening submission.
        :return: API response.
        """
        return self.screening_submissions_api.platform_screening_submissions_controller_get_screening_submission_using_id(
            screening_submission_id=screening_submission_id
        )

    def get_screening_submissions_of_org(
        self,
        org_alias: str,
        job_id: str,
        status: str,
        start_after: str,
        limit: int,
    ) -> Dict[str, Any]:
        """
        Get screening submissions of an organization.

        :param org_alias: The organization alias.
        :param job_id: The ID of the job.
        :param status: The status of the submissions.
        :param start_after: The starting point for pagination.
        :param limit: The number of submissions to return.
        :return: API response.
        """
        submissions_data = GetPlatformScreeningSubmissionsOfOrgDto(
            org_alias=org_alias,
            job_id=job_id,
            status=status,
            start_after=start_after,
            limit=limit,
        )
        return self.screening_submissions_api.platform_screening_submissions_controller_get_screening_submissions_of_org(
            get_platform_screening_submissions_of_org_dto=submissions_data
        )

    def get_screening_submissions_by_email_phone(
        self,
        email: str,
        phone: str,
        org_alias: str,
        job_id: str,
    ) -> Dict[str, Any]:
        """
        Get screening submissions by email or phone.

        :param email: The email of the candidate.
        :param phone: The phone number of the candidate.
        :param org_alias: The organization alias.
        :param job_id: The ID of the job.
        :return: API response.
        """
        return self.screening_submissions_api.platform_screening_submissions_controller_get_screening_submissions_using_email_phone(
            email=email,
            phone=phone,
            org_alias=org_alias,
            job_id=job_id,
        )

    def convert_audio_to_text(
        self,
        org_id: str,
        screening_submission_id: str,
        index: int,
        file: bytes,
        file_type: str,
    ) -> Dict[str, Any]:
        """
        Convert audio to text.

        :param org_id: The organization ID.
        :param screening_submission_id: The ID of the screening submission.
        :param index: The index of the question.
        :param file: The audio file.
        :param file_type: The type of the file.
        :return: API response.
        """
        return self.screening_submissions_api.platform_screening_submissions_controller_convert_audio_to_text(
            org_id=org_id,
            screening_submission_id=screening_submission_id,
            index=index,
            file=file,
            file_type=file_type,
        )

    def update_screening_submission_view_status(self, screening_submission_id: str) -> Dict[str, Any]:
        """
        Update screening submission view status.

        :param screening_submission_id: The ID of the screening submission.
        :return: API response.
        """
        return self.screening_submissions_api.platform_screening_submissions_controller_update_screening_submission_view_status(
            screening_submission_id=screening_submission_id
        )

    def update_screening_submission_status(
        self,
        screening_submission_ids: List[str],
        status: str,
    ) -> Dict[str, Any]:
        """
        Update screening submission status.

        :param screening_submission_ids: A list of screening submission IDs.
        :param status: The new status.
        :return: API response.
        """
        status_data = UpdatePlatformScreeningSubmissionsStatusDto(
            screening_submission_ids=screening_submission_ids,
            status=status,
        )
        return self.screening_submissions_api.platform_screening_submissions_controller_update_screening_submission_status(
            update_platform_screening_submissions_status_dto=status_data
        )

    def create_screening_stream_room(
        self,
        screening_job_id: str,
        screening_submission_id: str,
        curr_date_time_epoch: int,
    ) -> Dict[str, Any]:
        """
        Create a screening submission streaming room.

        :param screening_job_id: The ID of the screening job.
        :param screening_submission_id: The ID of the screening submission.
        :param curr_date_time_epoch: The current timestamp in epoch.
        :return: API response.
        """
        stream_data = CreatePlatformScreeningSubmissionStreamingRoomTokenDto(
            screening_job_id=screening_job_id,
            screening_submission_id=screening_submission_id,
            curr_date_time_epoch=curr_date_time_epoch,
        )
        return self.screening_submissions_api.platform_screening_submissions_controller_create_screening_stream_room(
            create_platform_screening_submission_streaming_room_token_dto=stream_data
        )
        
